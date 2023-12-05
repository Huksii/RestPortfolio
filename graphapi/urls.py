from django.urls import path
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView

from .schemes import schema

# Переопределяем метод execute_graphql_request для добавления дополнительной логики перед запросом GraphQL
class CustomGraphQLView(GraphQLView):
    def execute_graphql_request(self, request, data, query, variables, operation_name, show_graphiql=False):
        return super().execute_graphql_request(request, data, query, variables, operation_name, show_graphiql)
    
@login_required(login_url='admin')
def graphql_view(request):
    # Создаём экземпляр CustomGraphQLView и передаём ему объект schema graphiql=True
    view = CustomGraphQLView.as_view(graphiql=True, schema=schema)
    return view(request)

urlpatterns= [
    path('', graphql_view),
]