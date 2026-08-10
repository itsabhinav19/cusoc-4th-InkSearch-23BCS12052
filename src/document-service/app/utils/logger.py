import logging
from app.utils.logger import logger


logger.info(
    f"Starting hybrid search: query='{query}'"
)
logger.info(
    f"Semantic search returned {len(semantic_results)} results"
)
logger.info(
    f"Keyword search returned {len(keyword_documents)} results"
)
logger.info(
    f"Hybrid search completed with {len(response)} results"
)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("InkSearch")