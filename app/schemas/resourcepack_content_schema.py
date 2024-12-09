from app.schemas.content_schema import (
    CachedContent,
    CompiledContent,
    IntegrationContent,
    TypedContent,
)


class ResourcepackContent(IntegrationContent):
    pass


class TypedResourcepackContent(ResourcepackContent, TypedContent):
    pass


class ResourcepackCompiledContent(CompiledContent):
    pass


class ResourcepackCachedContent(ResourcepackCompiledContent, CachedContent):
    pass
