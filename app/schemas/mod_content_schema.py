from app.schemas.content_schema import (
    CachedContent,
    CompiledContent,
    IntegrationContent,
    TypedContent,
)


class ModContent(IntegrationContent):
    pass


class TypedModContent(ModContent, TypedContent):
    pass


class ModCompiledContent(CompiledContent):
    pass


class ModCachedContent(ModCompiledContent, CachedContent):
    pass
