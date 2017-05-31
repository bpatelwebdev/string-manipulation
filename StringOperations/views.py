from django.template.response import TemplateResponse
import operator


def StringOperation(request):
    return TemplateResponse(request, 'Form.html', {})

def Function_to_count(str, List_1 = [], Result = []):
    '''this function counts the repeated occurance of words/characters passed through List_1'''
    Dict_1 = {}  # creating an empty dictionart
    # convert list to set to eliminate duplicates
    Temp_set = set(List_1)
    del(Result)
    Result = []
    # each value in set is a key thus to assign null value initially the following loop is run
    for i in Temp_set:
        Dict_1.update({i: 0})  # assigns each key a value 0 initially
    # the following loop is to count the occurance of the word i.e key in the list created from paragraph
    for i in List_1:
        Dict_1[i] += 1

    # get the values of dictionary
    SortedValues = sorted(Dict_1.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(0,5):
        Result.append(SortedValues[i][0])
    del(List_1)
    return(Result)

def StringLogic(request):
    String_1 = request.POST['InputString']
    if len(String_1.split()) < 5:
        return TemplateResponse(request, 'Form.html', {'message': "Enter More Words", 'InputString': String_1})
    Words = Function_to_count('words', list(String_1.split(" ")))
    Characters = Function_to_count('characters',[i for i in list(String_1) if i != ' '])
    return TemplateResponse(request, 'ResultForm.html', {'words': Words, 'characters':Characters})


