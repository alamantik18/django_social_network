from rest_framework import generics, permissions, mixins, decorators, viewsets


class MixedPermission:
    """ Mixin permissions for action """

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class MixedPermissionViewSet(MixedPermission, viewsets.ViewSet):
    pass


class MixedPermissionGenericViewSet(MixedPermission, viewsets.GenericViewSet):
    pass


class CreateUpdateDestroy(MixedPermission,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    pass

class CreateRetrevieUpdateDestroy(MixedPermission,
                                  mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    pass