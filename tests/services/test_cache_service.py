from unittest.mock import AsyncMock, patch

import pytest

from app.services.cache_service import compile_cache_service_factory
from tests.conftest import instance_fixture, compiled_instance_fixture


@pytest.mark.asyncio
async def test_get_cached_instance(compiled_instance_fixture):
    cached_instance = compiled_instance_fixture

    cache_service = AsyncMock()
    cache_service.get.return_value = cached_instance.model_dump()

    compile_cache = await compile_cache_service_factory(cache_service)
    result = await compile_cache.get_cached_instance()

    assert result == cached_instance


@pytest.mark.asyncio
async def test_get_none_cached_instance():
    cache_service = AsyncMock()
    cache_service.get.return_value = None

    compile_cache = await compile_cache_service_factory(cache_service)
    result = await compile_cache.get_cached_instance()

    assert result is None


@pytest.mark.asyncio
async def test_get_valid_cached_instance(instance_fixture, compiled_instance_fixture):
    instance = instance_fixture
    cached_instance = compiled_instance_fixture

    cache_service = AsyncMock()
    cache_service.get.return_value = cached_instance.model_dump()

    with patch("app.services.cache_service.hash_dict", return_value=cached_instance.instance_hash):
        compile_cache = await compile_cache_service_factory(cache_service)
        result = await compile_cache.get_valid_cached_instance(instance)

    assert result == cached_instance
    cache_service.get.assert_called_once_with("instance")


@pytest.mark.asyncio
async def test_get_not_valid_cached_instance(instance_fixture, compiled_instance_fixture):
    instance = instance_fixture
    cached_instance = compiled_instance_fixture

    cache_service = AsyncMock()
    cache_service.get.return_value = cached_instance.model_dump()

    with patch("app.services.cache_service.hash_dict", return_value="dummy_cache"):
        compile_cache = await compile_cache_service_factory(cache_service)
        result = await compile_cache.get_valid_cached_instance(instance)

    assert result is None
    cache_service.get.assert_called_once_with("instance")
