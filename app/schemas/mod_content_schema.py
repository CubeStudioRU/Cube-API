from app.schemas.content_schema import BaseContent, CompiledContent, CachedContent, TypedContent


class ModContent(BaseContent):
    pass


class TypedModContent(ModContent, TypedContent):
    pass


class ModCompiledContent(CompiledContent):
    pass


class ModCachedContent(ModCompiledContent, CachedContent):
    pass
