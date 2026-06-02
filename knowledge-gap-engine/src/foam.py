import foam
from config.settings import OTEL_FOAM_COLLECTOR_BEARER_TOKEN, IS_PRODUCTION

foam.init(
    service_name='knowledge-gap-engine',
    is_production=IS_PRODUCTION,
    api_key=f'Bearer {OTEL_FOAM_COLLECTOR_BEARER_TOKEN}',
)