import json
from unicodedata import category

import graphene
from graphene.relay import Node
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from graphql_auth import mutations
from graphql_auth.schema import MeQuery, UserNode, UserQuery

from ..content.models import Category, Document, Image, Page

### Auth ###


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()


### Content ###


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("title", "slug", "in_navbar", "pages")


class PageType(DjangoObjectType):
    class Meta:
        model = Page
        # interfaces = (Node,)
        fields = (
            "title",
            "slug",
            "content",
            "in_navbar",
            "type",
            "category",
            "updated_at",
            "author",
            "profile_image",
        )

    author = graphene.Field(UserNode)
    content = GenericScalar(
        resolver=lambda Page, resolve_obj: json.loads(Page.content.delta)
    )
    # content = graphene.JSON(
    #     resolver=lambda Page, resolve_obj: str(Page.content.html)
    # )


# \"delta\", \"field\", \"html\", \"instance\", \"json_string\", \"plain\", \"quill\

################################################################


class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_pages = graphene.List(PageType)
    page_by_slug = graphene.Field(PageType, slug=graphene.String())
    last_10_edited_pages = graphene.List(PageType)

    all_categories = graphene.List(CategoryType)
    category_by_slug = graphene.Field(CategoryType, slug=graphene.String())

    page_by_category_and_slug = graphene.Field(
        PageType, category=graphene.String(), slug=graphene.String()
    )

    def resolve_all_pages(root, info):
        return Page.objects.all()

    def resolve_page_by_slug(root, info, slug):
        return Page.objects.get(slug=slug)

    def resolve_last_10_edited_pages(root, info):
        return Page.objects.all().order_by("-updated_at")[:10]

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category_by_slug(root, info, slug):
        return Category.objects.get(slug=slug)

    def resolve_page_by_category_and_slug(root, info, category, slug):
        return Page.objects.get(category__slug=category, slug=slug)


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
