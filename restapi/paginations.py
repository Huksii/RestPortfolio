from rest_framework.pagination import PageNumberPagination

class ContactPagination(PageNumberPagination):
    #Количество объектов на странице
    page_size = 100
    # Параметр запроса для указания количества объектов на странице(встроенный)
    page_size_query_param = 'page_size'
    # Максимальный размер страницы который можно указать в запросе
    max_page_size = 100
    # Параметр запроса для указания номера страницы(встроенный)
    page_query_param = 'p'
    # Обозначение последней страницы
    last_page_strings = ['end']