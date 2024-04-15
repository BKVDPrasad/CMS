import graphene
from graphene_django import DjangoObjectType  # used to change Django object into a format that is readable by GraphQL
from app3.models import Item


class ContactType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        """ describing about class """
        model = Item
        field = "__all__"


class Query(graphene.ObjectType):
    # query ContactType to get list of contacts
    list_contact = graphene.List(ContactType)
    read_contact = graphene.Field(ContactType, id=graphene.Int())  # id=graphene.Int() gives id an integer datatype

    def resolve_list_contact(root, info):
        """ test """
        # We can easily optimize query count in the resolve method
        return Item.objects.all()

    def resolve_read_contact(root, info, mid):
        # get data where id in the database = id queried from the frontend
        return Item.objects.get(id=mid)


class ContactMutation(graphene.Mutation):
    class Arguments:
        """test something"""
        # Add fields you would like to create. This will corelate with the ContactType fields above.
        id = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        price = graphene.Decimal()

    contact = graphene.Field(ContactType)  # define the class we are getting the fields from

    @classmethod
    def mutate(cls, root, info, mid, name, description, price):
        """ test some"""
        # function that will save the data
        contact = Item(name=name, description=description, price=price)  # accepts all fields
        contact.save()  # d=save the contact

        get_contact = Item.objects.get(id=mid)
        get_contact.name = name  # override name
        get_contact.description = description  # override phone_number
        get_contact.price = price
        get_contact.save()
        return ContactMutation(contact=get_contact)


class Mutation(graphene.ObjectType):
    # keywords that will be used to do the mutation in the frontend
    create_contact = ContactMutation.Field()
    update_contact = ContactMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)  # Tell the schema about the mutation you just created.
