
## Understanding the Data about AGA

<ins>REPO: buildwithai-foodchain</ins>

- Please clone, fork, pull requests as you need to.
- Put your questions into the challenge slack channel.

Let’s spend some time understanding AGA’s data, which we will be using as part of this journey, with a number of viewpoints. The focus with this sample dataset, is to keep it minimalistic, fun and useful to exercise AI technologies and techniques which could be applied for many different benefits. The purpose is to quickly identify what techniques can help.

The datasets provide data for the two ends of the spectrum with respect to the Supply Chain. This is more like a Surprise Chain.

### Partner Donations

The donations are provided typically by Supermarket organisations like 'FoodieLand','LoMarket','Grocertown', which could easily be extended to extra Partners, some of which could be specialist food providers.

The Partner Donations Dataset consists of two files:
orderHeaderDonations.csv – a dataset of donations provided by partners
orderItemsDonations.csv – a dataset of the items for each donation

#### orderHeaderDonations.csv
| OrderID | PartnerID | OrderTotal | OrderDate | PartnerName | PartnerGeoLat | PartnerGeoLon |
| -- | -- | -- | -- | -- | -- | -- |
| 200501  | 190053 | 2000 | 01/10/2021 | FoodieLand| -34.923321 | 138.602142 |

#### orderItemsDonations.csv
| OrderID | OrderItemID	| ProductType	| ProductItem	| ProductPeriod	| ProductDetails | ProductStorage	| Quantity |
| -- | -- | -- | -- | -- | -- | -- | -- |
| 200501 | 953 | DAIRY | Milk Box | 2 Weeks | Unopened | Refrigeration | 80 |

The sample dataset provides deliveries from Partner Donations over a 90 day period, with a variety of types of orders, with varying quantities.

### Community Requests

The request for donations come from people in need in the local area, which we have kept to 20 distinct community families, who could be requesting food 4 to 10 times in a month.

The Community Request Dataset consists of two files:
orderHeaderRequests.csv – a dataset of requests from families
orderItemsRequests.csv – a dataset of the items for each request

#### orderHeaderRequests.csv
| OrderID | CustomerID | OrderTotal	| OrderDate | CustomerName | CustomerGeoLat	| CustomerGeoLon |
| -- | -- | -- | -- | -- | -- | -- |
| 200501 | 190053 | 200 |	01/10/2021 |  FoodieLand | -34.923321 | 138.602142 |

#### orderItemsRequests.csv
| OrderID	| OrderItemID	| ProductType	|  ProductItem | ProductPeriod | ProductDetails	|  ProductStorage	|
| -- | -- | -- | -- | -- | -- | -- |
| 200501 | 953 | DAIRY | Milk Box | 	2 Weeks | Unopened | Refrigeration |

The sample dataset provides requests from the community over a 90 day period, with a variety of types of orders, with varying quantities.

