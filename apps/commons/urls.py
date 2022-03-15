from rest_framework import routers

from apps.commons.views import CountryView, RegionView, SubRegionView, DistrictView

router = routers.DefaultRouter()
router.register('country', CountryView)
router.register('region', RegionView)
router.register('subregion', SubRegionView)
router.register('district', DistrictView)
urlpatterns = router.urls
