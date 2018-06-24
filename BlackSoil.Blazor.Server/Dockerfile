FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY BlackSoil.Blazor.Server/BlackSoil.Blazor.Server.csproj BlackSoil.Blazor.Server/
COPY BlackSoil.Blazor.Client/BlackSoil.Blazor.Client.csproj BlackSoil.Blazor.Client/
COPY BlackSoil.Blazor.Shared/BlackSoil.Blazor.Shared.csproj BlackSoil.Blazor.Shared/
RUN dotnet restore BlackSoil.Blazor.Server/BlackSoil.Blazor.Server.csproj
COPY . .
WORKDIR /src/BlackSoil.Blazor.Server
RUN dotnet build BlackSoil.Blazor.Server.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish BlackSoil.Blazor.Server.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "BlackSoil.Blazor.Server.dll"]
