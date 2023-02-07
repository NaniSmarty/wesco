

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



getgame_schema_dict2 = {
            "200": openapi.Response(
                description="success",
                examples={
                    "application/json": {
                        "status": 0,
                        "description": "Success",
                        "generator_datetime": "20221119 06:52:18",
                        "result": [
                            {
                                "drawid": 233,
                                "drawdate": "20221119",
                                "drawtime": "09:55:00",
                                "drawname": "WESCO FORTUNE",
                                "closetime": "09:50:00"
                            },
                            {
                                "drawid": 240,
                                "drawdate": "20221119",
                                "drawtime": "09:55:00",
                                "drawname": "WESCO FORTUNE MACH",
                                "closetime": "09:50:00"
                            },
                            {
                                "drawid": 139,
                                "drawdate": "20221119",
                                "drawtime": "11:55:00",
                                "drawname": "WESCO DOLLAR",
                                "closetime": "11:50:00"
                            },
                            {
                                "drawid": 176,
                                "drawdate": "20221119",
                                "drawtime": "11:55:00",
                                "drawname": "WESCO DOLLAR MACH",
                                "closetime": "11:50:00"
                            },
                            {
                                "drawid": 247,
                                "drawdate": "20221119",
                                "drawtime": "13:55:00",
                                "drawname": "WESCO TRILLION",
                                "closetime": "13:50:00"
                            },
                            {
                                "drawid": 254,
                                "drawdate": "20221119",
                                "drawtime": "13:55:00",
                                "drawname": "WESCO TRILLION MACH",
                                "closetime": "13:50:00"
                            },
                            {
                                "drawid": 169,
                                "drawdate": "20221119",
                                "drawtime": "15:55:00",
                                "drawname": "WESCO SOCCER MACH",
                                "closetime": "15:50:00"
                            },
                            {
                                "drawid": 132,
                                "drawdate": "20221119",
                                "drawtime": "15:55:00",
                                "drawname": "WESCO SOCCER",
                                "closetime": "15:50:00"
                            },
                            {
                                "drawid": 289,
                                "drawdate": "20221119",
                                "drawtime": "19:45:00",
                                "drawname": "WESCO BONANZA",
                                "closetime": "19:40:00"
                            },
                            {
                                "drawid": 290,
                                "drawdate": "20221119",
                                "drawtime": "19:45:00",
                                "drawname": "WESCO BONANZA MACH",
                                "closetime": "19:40:00"
                            },
                            {
                                "drawid": 273,
                                "drawdate": "20221119",
                                "drawtime": "19:55:00",
                                "drawname": "Wesco Weekend",
                                "closetime": "19:50:00"
                            },
                            {
                                "drawid": 279,
                                "drawdate": "20221119",
                                "drawtime": "19:55:00",
                                "drawname": "Wesco Weekend Mach",
                                "closetime": "19:50:00"
                            },
                            {
                                "drawid": 191,
                                "drawdate": "20221119",
                                "drawtime": "22:30:00",
                                "drawname": "WESCO BANK",
                                "closetime": "22:25:00"
                            },
                            {
                                "drawid": 198,
                                "drawdate": "20221119",
                                "drawtime": "22:30:00",
                                "drawname": "WESCO BANK MACH",
                                "closetime": "22:25:00"
                            }
                        ]
                    }
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }




cancelticket_schema_dict4 = {
            "200": openapi.Response(
                description="success",
                examples={
                    "application/json":{}
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }




checkwinner_schema_dict7 = {
            "200": openapi.Response(
                description="success",
                examples={
                    "application/json": {
                        "status": 0,
                        "description": "Success",
                        "generator_datetime": "~20221119 08:03:15",
                        "Info": [
                            {
                                "Ticket_id": "0805923232631841",
                                "Amount": "48000"
                            }
                        ]
                    }
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }




ticketstatus_schema_dict6 = {
            "200": openapi.Response(
                description="success",
                examples={
                    "application/json": {
                        "status": 0,
                        "description": "Success",
                        "generator_datetime": "20221119 07:56:18",
                        "Ticket_status": "Winning not Claimed the Ticket",
                        "Amount": 200
                    }
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }




sellticket_schema_dict3 = {
            "200": openapi.Response(
                description="success",
                examples={                                    
                        "application/json": {
                            "Result": {
                                "status": 0,
                                "description": "Success",
                                "draws": {
                                    "drawId": 243,
                                    "Drawname": "WESCO BANK",
                                    "drawDate": "20221119",
                                    "drawtime": "22:30:00",
                                    "purchasedate": "20221119",
                                    "purchasedtime": "12:38:20",
                                    "totalamount": 200,
                                    "TransactionId": "999998",
                                    "TikcetId": "0805923234550021",
                                    "infoarray": [
                                        {
                                            "Betamount": "200",
                                            "Info": "01;02",
                                            "Bettypes": "Permutation2"
                                        }
                                    ]
                                }
                            }
                        }
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }

response_schema_dict6 = {
    "200": openapi.Response(
        description="success",
        examples={
            "application/json": {
                            "Result": {
                                "status": 0,
                                "description": "Success",
                                "generator_datetime": "20220706 10:42:32",
                                "Ticket_status": "Sold Ticket"
                            }
                        }
        }
    ),
    "201": openapi.Response(
            description="success",
            examples={
                "application/json": {
                    "Result": {
                        "status": 1,
                        "description": "Invalid TransactionID"
                    }
                }
            }
        ),
    "400": openapi.Response(
        description="Required Parameters Error",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Required Parameters Error"
            }
        }
    ),
    "406": openapi.Response(
        description="Backend Validation Error",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Backend Validation Error"
            }
        }
    ),
    "422": openapi.Response(
        description="Unprocessable Entity",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Unprocessable Entity"
            }
        }
    ),
    "500": openapi.Response(
        description="Required Parameters Error",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Internal Server Error"
            }
        }
    )
}


response_schema_dict7 = {
            "200": openapi.Response(
                description="success",
                examples={
                    "application/json": {
                        "Result": {
                            "status": 0,
                            "description": "Success",
                            "generator_datetime": "~20220917 10:57:16",
                            "Info": [
                                {
                                    "Ticket_id": "7033222583233167",
                                    "Amount": "60000"
                                }
                            ]
                        }
                    }
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }


response_schema_dict8 = {
            "200": openapi.Response(
                description="success",
                examples={
                    "application/json": {
                        "Result": {
                            "status": 0,
                            "description": "Success",
                            "generator_datetime": "~20220917 11:15:38",
                            "Info": "Transaction has been Claimed successfully"
                        }
                    }
                }
            ),
            "400": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Required Parameters Error"
                    }
                }
            ),
            "406": openapi.Response(
                description="Backend Validation Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Backend Validation Error"
                    }
                }
            ),
            "422": openapi.Response(
                description="Unprocessable Entity",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Unprocessable Entity"
                    }
                }
            ),
            "500": openapi.Response(
                description="Required Parameters Error",
                examples={
                    "application/json": {
                        "Status": "1",
                        "Message": "Internal Server Error"
                    }
                }
            )
        }
checkwinner_schema_dict5= {
    "200": openapi.Response(
        description="success",
        examples={
            "application/json": {

                "Result": {
                    "status": 0,
                    "description": "Success",
                    "generator_datetime": "~20220505 11:25:14",
                    "draws": {
                        "saledate": "20220408",
                        "saletime": "15:54:54",
                        "info": [
                            {
                                "Ticketid": "20220408201306E2A",
                                "WinAmount": "75"
                            },
                            {
                                "Ticketid": "20220408202024E2B",
                                "WinAmount": "75"
                            },

                            {
                                "Ticketid": "202204082024541D3",
                                "WinAmount": "75"
                            }
                        ]
                    }
                }
            }
        }
    ),
    "400": openapi.Response(
        description="Required Parameters Error",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Required Parameters Error"
            }
        }
    ),
    "406": openapi.Response(
        description="Backend Validation Error",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Backend Validation Error"
            }
        }
    ),
    "422": openapi.Response(
        description="Unprocessable Entity",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Unprocessable Entity"
            }
        }
    ),
    "500": openapi.Response(
        description="Required Parameters Error",
        examples={
            "application/json": {
                "Status": "1",
                "Message": "Internal Server Error"
            }
        }
    )
}




