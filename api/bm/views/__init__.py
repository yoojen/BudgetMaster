from flask  import Blueprint
bm_views = Blueprint("bm_views", __name__, url_prefix="/api/bm/")

from api.bm.views.users import *
from api.bm.views.expenses import *