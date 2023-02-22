import graphene
from graphene_django import DjangoObjectType

from users.models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id", "username", "email")


class Query(graphene.ObjectType):
    profiles = graphene.List(ProfileType)
    profile_by_id = graphene.Field(ProfileType, id=graphene.UUID(required=True))

    def resolve_profiles(root, info, **kwargs):
        return Profile.objects.all()

    def resolve_profile_by_id(root, info, id):
        return Profile.objects.get(pk=id)


schema = graphene.Schema(query=Query)
