from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    keyspace_hits = cache._cache.get_client().info().get('keyspace_hits', 0)
    keyspace_misses = cache._cache.get_client().info().get('keyspace_misses', 0)
    total_requests = keyspace_hits + keyspace_misses
    hit_ratio = keyspace_hits / total_requests if total_requests > 0 else 0
    logger.error(f"Cache metrics - Hits: {keyspace_hits}, Misses: {keyspace_misses}, Hit Ratio: {hit_ratio}")
    return {
        'keyspace_hits': keyspace_hits,
        'keyspace_misses': keyspace_misses,
        'hit_ratio': hit_ratio
    }
