from works_single_view.works_single_view.models import Works
from rest_framework import serializers


class WorksForCsvSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()


    class Meta:
        model = Works
        fields = ('id', 'title', 'iswc', 'source', 'contributors')

    def get_contributors(self, works):
        contributors = []
        for contributor in works.contributors.all():
            contributors.append(contributor.name)

        return "|".join(contributors)

class WorksSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()


    class Meta:
        model = Works
        fields = ('id', 'title', 'iswc', 'source', 'contributors')

    def get_contributors(self, works):
        contributors = []
        for contributor in works.contributors.all():
            contributors.append(contributor.name)

        return contributors       