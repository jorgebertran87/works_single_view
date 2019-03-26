from works_single_view.works_single_view.models import Works
from rest_framework import viewsets
from works_single_view.works_single_view.serializers import WorksSerializer, WorksForCsvSerializer
from rest_pandas import PandasView


class WorksSingleViewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows Works Single View metadata.
    """
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

class ExportWorksSingleViewView(PandasView):

    queryset = Works.objects.all()
    serializer_class = WorksForCsvSerializer    



