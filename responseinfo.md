# Estrutura do JSON — Geocodificação Google Maps

O JSON representa o resultado de uma consulta de geocodificação (*Geocoding*), transformando um endereço textual em informações estruturadas: coordenadas, precisão, limites geográficos e componentes cadastrais.

## 1. Estrutura principal

| Campo | Significado |
|---|---|
| `id` | Identificador do registro na base de dados. |
| `endereco_original` | Endereço enviado à API. |
| `resposta` | Objeto contendo o resultado da geocodificação. |

## 2. Resultado da consulta (`results`)

Lista de correspondências encontradas pela API.

| Campo | Significado |
|---|---|
| `place` | Referência do recurso no Google Maps. |
| `placeId` | Identificador único do lugar no Google Maps. |
| `types` | Classificação geral do resultado. |

**Observação:** `results` é uma lista (`array`), mesmo quando contém apenas um resultado.

## 3. Coordenadas (`location`)

| Campo | Significado |
|---|---|
| `latitude` | Latitude do ponto geográfico. |
| `longitude` | Longitude do ponto geográfico. |

Representam a localização identificada pela API, não necessariamente o centro geométrico do imóvel.

## 4. Precisão (`granularity`)

Indica o nível de precisão da correspondência geográfica.

| Valor | Significado |
|---|---|
| `ROOFTOP` | Localização no nível da edificação. |
| `RANGE_INTERPOLATED` | Posição estimada por interpolação na rua. |
| `GEOMETRIC_CENTER` | Centro geométrico de uma área ou geometria. |
| `APPROXIMATE` | Localização aproximada. |

`ROOFTOP` é desejável para geocodificação imobiliária, mas não garante correspondência exata com o lote ou entrada do imóvel.

## 5. Limites geográficos (`viewport` e `bounds`)

Ambos utilizam coordenadas `low` e `high`, representando os limites de uma área geográfica.

| Campo | Finalidade |
|---|---|
| `viewport` | Área recomendada para enquadrar o resultado em um mapa. |
| `bounds` | Extensão geográfica associada ao objeto identificado. |

Não confundir esses campos com `location`, que representa um ponto geográfico.

## 6. Endereço formatado (`formattedAddress`)

Endereço completo, normalizado e formatado pela API.

Útil para:
- Padronização dos endereços.
- Comparação com o endereço original.
- Identificação de divergências.
- Substituição de endereços inconsistentes.

## 7. Endereço estruturado (`postalAddress`)

Apresenta os componentes postais e administrativos do endereço.

| Campo | Significado |
|---|---|
| `regionCode` | Código do país (ex.: BR). |
| `languageCode` | Idioma associado à representação postal. |
| `postalCode` | CEP. |
| `administrativeArea` | Estado ou unidade administrativa. |
| `locality` | Município/cidade. |
| `sublocality` | Subdivisão territorial, como bairro. |
| `addressLines` | Linhas do endereço. |

## 8. Componentes do endereço (`addressComponents`)

Lista de elementos individuais que compõem o endereço.

| Campo | Significado |
|---|---|
| `longText` | Nome ou valor completo. |
| `shortText` | Forma abreviada. |
| `types` | Classificações do componente. |
| `languageCode` | Idioma, quando disponível. |

Principais classificações:

| Tipo | Significado |
|---|---|
| `street_number` | Número do imóvel. |
| `route` | Logradouro. |
| `sublocality` | Subdivisão territorial. |
| `sublocality_level_1` | Primeiro nível de subdivisão territorial. |
| `administrative_area_level_2` | Divisão administrativa de segundo nível. |
| `administrative_area_level_1` | Divisão administrativa de primeiro nível. |
| `country` | País. |
| `postal_code` | CEP. |
| `political` | Entidade ou divisão administrativa. |

**Importante:** `types` é uma lista porque um mesmo componente pode possuir várias classificações. Portanto, é preferível identificar os componentes pelo conteúdo de `types`, e não pela posição na lista.

## 9. Classificação geral (`results[0].types`)

Classifica o resultado completo da geocodificação.

| Tipo | Significado |
|---|---|
| `premise` | Edificação ou propriedade identificada. |
| `street_address` | Endereço específico de uma rua. |

Não confundir com `addressComponents[n].types`, que classifica cada componente individualmente.

---

## 10. Recomendação para armazenamento

Para uma base de dados imobiliários, recomenda-se organizar as informações em três grupos:

### Identificação e qualidade
- `placeId`
- `granularity`
- `types`

### Dados geográficos
- `latitude`
- `longitude`
- `bounds`
- `viewport`

### Dados cadastrais
- `formattedAddress`
- `postalCode`
- `administrativeArea`
- `locality`
- `sublocality`
- `addressComponents`

### Recomendação final

Manter também o JSON original em uma coluna permite recuperar informações que futuramente possam ser necessárias, sem precisar consultar novamente a API.

**Atenção:** `ROOFTOP` indica precisão geográfica no nível da edificação, mas não comprova a existência jurídica, a titularidade ou a correspondência cadastral do imóvel.