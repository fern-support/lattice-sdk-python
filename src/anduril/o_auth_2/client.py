# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOAuth2Client, RawOAuth2Client
from .types.get_token_request_grant_type import GetTokenRequestGrantType
from .types.get_token_response import GetTokenResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class OAuth2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuth2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuth2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuth2Client
        """
        return self._raw_client

    def get_token(
        self,
        *,
        grant_type: GetTokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTokenResponse:
        """
        Exchange authorization code, refresh token, client credentials, or resource owner credentials for an access token

        Parameters
        ----------
        grant_type : GetTokenRequestGrantType
            The type of grant being requested

        code : typing.Optional[str]
            The authorization code (required for authorization_code grant type)

        redirect_uri : typing.Optional[str]
            The redirect URI (required for authorization_code grant type)

        client_id : typing.Optional[str]
            The client identifier

        client_secret : typing.Optional[str]
            The client secret

        refresh_token : typing.Optional[str]
            The refresh token (required for refresh_token grant type)

        username : typing.Optional[str]
            The resource owner username (required for password grant type)

        password : typing.Optional[str]
            The resource owner password (required for password grant type)

        scope : typing.Optional[str]
            The scope of the access request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokenResponse
            Access token response

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.o_auth_2.get_token(
            grant_type="authorization_code",
        )
        """
        _response = self._raw_client.get_token(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            username=username,
            password=password,
            scope=scope,
            request_options=request_options,
        )
        return _response.data


class AsyncOAuth2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuth2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuth2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuth2Client
        """
        return self._raw_client

    async def get_token(
        self,
        *,
        grant_type: GetTokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTokenResponse:
        """
        Exchange authorization code, refresh token, client credentials, or resource owner credentials for an access token

        Parameters
        ----------
        grant_type : GetTokenRequestGrantType
            The type of grant being requested

        code : typing.Optional[str]
            The authorization code (required for authorization_code grant type)

        redirect_uri : typing.Optional[str]
            The redirect URI (required for authorization_code grant type)

        client_id : typing.Optional[str]
            The client identifier

        client_secret : typing.Optional[str]
            The client secret

        refresh_token : typing.Optional[str]
            The refresh token (required for refresh_token grant type)

        username : typing.Optional[str]
            The resource owner username (required for password grant type)

        password : typing.Optional[str]
            The resource owner password (required for password grant type)

        scope : typing.Optional[str]
            The scope of the access request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokenResponse
            Access token response

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.o_auth_2.get_token(
                grant_type="authorization_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_token(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            username=username,
            password=password,
            scope=scope,
            request_options=request_options,
        )
        return _response.data
