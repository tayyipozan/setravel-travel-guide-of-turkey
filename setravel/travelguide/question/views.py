from django.shortcuts import render, get_object_or_404
from .models import Questions
from places.models import Place, PlaceDetail

answers = {}
noneques = set()


def showquestion(request, id, answers):
    questions = get_object_or_404(Questions, id=id)
    answr = None
    for question, ans in answers.items():
        if question == id:
            answr = ans
    context = {
        'questions': questions,
        'answr': answr,
    }
    return render(request, 'question/questions.html', context)


def question(request, id):
    if request.POST.get('qst'):
        if request.POST.get('qst') == "1":
            answer = request.POST.get('answer')
            answers[id] = answer
            if id == 1:
                id = 2
                return showquestion(request, id, answers)
            elif id == 2:
                if answer == 'Activity' or answer == 'Historical':
                    id = 3
                    return showquestion(request, id, answers)
                elif answer == 'Eating':
                    id = 6
                    return showquestion(request, id, answers)
                elif answer == 'Hotels':
                    id = 8
                    return showquestion(request, id, answers)
                elif answer == 'Relax':
                    id = 5
                    return showquestion(request, id, answers)
            else:
                if answers[2] == 'Activity' and answer == 'Open Area':
                    id = 4
                    return showquestion(request, id, answers)
                elif answers[2] == 'Activity' and answer == 'Covered Area':
                    return final(request, answers)
                elif answers[2] == 'Relax' and (answer == 'Natural' or answer == 'Architectural'):
                    return final(request, answers)
                elif answers[2] == 'Historical' and (answer == 'Open Area' or answer == 'Covered Area'):
                    id = 5
                    return showquestion(request, id, answers)
                elif answers[2] == 'Historical' and (answer == 'Natural' or answer == 'Architectural'):
                    return final(request, answers)
                elif answers[2] == 'Eating' and (answer == 'Breakfast' or answer == 'Dinner'):
                    id = 7
                    return showquestion(request, id, answers)
                elif answers[2] == 'Eating' and (answer == 'Local' or answer == 'Franchise'):
                    return final(request, answers)
                elif answers[2] == 'Hotels' and (answer == 'Boutique' or answer == 'Luxury'):
                    id = 9
                    return showquestion(request, id, answers)
                elif answers[2] == 'Hotels' and (answer == 'Yes' or answer == 'No'):
                    return final(request, answers)
        else:
            answers.pop(id, None)
            ids = list(answers.keys())
            id = ids[-1]
            return showquestion(request, id, answers)
    else:
        id = 1
        return showquestion(request, id, answers)


def final(request, answers):
    print(answers)
    region, category, area, temp, structure, meal, restaurant, hotel, sea = None, None, None, None, None, None, None, None, None
    for qid, answer in answers.items():
        if qid == 1:
            region = answer
        elif qid == 2:
            category = answer
        elif qid == 3:
            area = answer
        elif qid == 4:
            temp = answer
        elif qid == 5:
            structure = answer
        elif qid == 6:
            meal = answer
        elif qid == 7:
            restaurant = answer
        elif qid == 8:
            hotel = answer
        elif qid == 9:
            sea = answer
    detailplaces = PlaceDetail.objects.filter(region=region, area=area,temp=temp,structure=structure,category=category, meal=meal, restaurant=restaurant, hotel=hotel, sea=sea)
    print(detailplaces)
    places=Place.objects.all().order_by('title')
    context = {
        'places': places,
        'detailplaces': detailplaces,
    }
    answers.clear()
    return render(request,'places/list.html',context)
