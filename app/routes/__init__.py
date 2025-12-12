from fastapi import APIRouter

from app.routes.auth_routes import router as auth_router
from app.routes.utilisateurs_routes import router as utilisateurs_router
from app.routes.catalogue_routes import router as catalogue_router
from app.routes.panier_routes import router as panier_router
from app.routes.commandes_routes import router as commandes_router
from app.routes.admin_routes import router as admin_router

router_api = APIRouter(prefix="/api")

router_api.include_router(auth_router, prefix="/auth", tags=["auth"])
router_api.include_router(utilisateurs_router, prefix="/utilisateurs", tags=["utilisateurs"])
router_api.include_router(catalogue_router, prefix="/catalogue", tags=["catalogue"])
router_api.include_router(panier_router, prefix="/panier", tags=["panier"])
router_api.include_router(commandes_router, prefix="/commandes", tags=["commandes"])
router_api.include_router(admin_router, prefix="/admin", tags=["admin"])
