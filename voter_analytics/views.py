from django.views.generic import ListView, DetailView
from .models import Voter  
from django.db.models import Q, Count  
from datetime import date  
import plotly.express as px
from plotly.offline import plot

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

class VoterGraphsView(ListView): 
    ''' A view to show the graphing data for voters '''
    model = Voter
    template_name = 'voter_analytics/graphs.html'
    context_object_name = 'voters'

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
        queryset = self.get_queryset()

        # Histogram of Voters by Year of Birth
        birth_years = queryset.values_list('date_of_birth', flat=True)
        birth_years = [dob.year for dob in birth_years]
        fig1 = px.histogram(x=birth_years, nbins=20, labels={'x': 'Year of Birth'}, title="Distribution of Voters by Year of Birth")
        context['birth_year_histogram'] = plot(fig1, output_type='div')

        # Pie Chart of Voters by Party Affiliation
        party_counts = queryset.values('party_affiliation').annotate(count=Count('party_affiliation'))
        fig2 = px.pie(party_counts, names='party_affiliation', values='count', title="Voters by Party Affiliation", width=600, height=600)
        context['party_affiliation_pie'] = plot(fig2, output_type='div')

        # Histogram of Voters by Election Participation
        elections = ['v20_state', 'v21_town', 'v21_primary', 'v22_general', 'v23_town']
        participation_counts = {election: queryset.filter(**{election: True}).count() for election in elections}
        fig3 = px.bar(x=list(participation_counts.keys()), y=list(participation_counts.values()), labels={'x': 'Election', 'y': 'Count'}, title="Voters by Election Participation")
        context['election_participation_histogram'] = plot(fig3, output_type='div')

        # Additional context for filtering options
        context['years'] = range(1913, 2006)  # Year range for birth dates
        context['voter_scores'] = range(1, 6)  # Range of voter scores (1 to 5)
        context['party_affiliations'] = Voter.objects.values_list('party_affiliation', flat=True).distinct()
        return context