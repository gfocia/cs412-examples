from django.views.generic import ListView, DetailView
from .models import Voter  
from django.db.models import Q  
from datetime import date  

class VoterListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voter_list.html'
    context_object_name = 'voters'
    paginate_by = 100  

    def get_queryset(self):
        queryset = Voter.objects.all()
        party_affiliation = self.request.GET.get('party_affiliation')
        min_dob = self.request.GET.get('min_dob')
        max_dob = self.request.GET.get('max_dob')
        voter_score = self.request.GET.get('voter_score')

        if party_affiliation:
            queryset = queryset.filter(party_affiliation=party_affiliation)

        if min_dob:
            queryset = queryset.filter(date_of_birth__gte=date(int(min_dob), 1, 1))

        if max_dob:
            queryset = queryset.filter(date_of_birth__lte=date(int(max_dob), 12, 31))

        if voter_score:
            queryset = queryset.filter(voter_score=int(voter_score))

        for election_field in ['v20_state', 'v21_town', 'v21_primary', 'v22_general', 'v23_town']:
            if self.request.GET.get(election_field) == 'true':
                queryset = queryset.filter(**{election_field: True})

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = range(1913, 2006)  # Year range for birth dates
        context['voter_scores'] = range(1, 6)  # Range of voter scores (1 to 5)
        context['party_affiliations'] = Voter.objects.values_list('party_affiliation', flat=True).distinct()
        return context

class VoterDetailView(DetailView): 
    ''' A view to show a page for a single Voter record '''
    model = Voter 
    template_name = 'voter_analytics/voter_detail.html'
    context_object_name = 'voter'