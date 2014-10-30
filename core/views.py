from django.shortcuts import render

# Create your views here.

def get_elements(school_id=None, team_id=None, username=None):
	if school_id is None:
		return render(request, "map.html")
	elif team_id is None:
		return render(request, "school.html")
	elif username is None:
		return render(request, "team.html")
	else:
		return render(request, "profile.html")