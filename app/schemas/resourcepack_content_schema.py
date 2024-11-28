from app.schemas.content_schema import CompiledContent, CachedContent, TypedContent, IntegrationContent


class ResourcepackContent(IntegrationContent):
    pass


class TypedResourcepackContent(ResourcepackContent, TypedContent):
    pass


class ResourcepackCompiledContent(CompiledContent):
    pass


class ResourcepackCachedContent(ResourcepackCompiledContent, CachedContent):
    pass
