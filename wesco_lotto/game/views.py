from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
# import psycopg2
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import pymssql
from datetime import datetime as dt
# from .log import *
from .response import *
from .credentials import *

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class getgameAPIview(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    # queryset = getgame.objects.all()
    serializer_class = getgameSerializer

    @swagger_auto_schema(request_body=getgameSerializer, responses=getgame_schema_dict2)
    def post(self, request):
        try:
            global error_key
            datas = request.data
            client_ip = visitor_ip_address(request)
            ##io_log.info("  getgame  Req : " + str(datas) + " | " + str(client_ip))
            serializer = getgameSerializer(data=datas)
            if not serializer.is_valid():
                out = {"success": False, "errors": serializer.errors}
                ##io_log.info(" getgame  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            APIToken = self.request.META.get('HTTP_APIKEY', None)
            AgentID = serializer.validated_data['agent_id']
            error_key = str(AgentID)
            conn = pymssql.connect(database=db_name, user=user_name, password=pwd,
                                   host=host_ip, port=port_ip)
            cursor = conn.cursor()
            query = f"Exec CLI_MYLotto_Get_GameInfo '{APIToken}','{AgentID}';"
            ##io_log.info("  getgame  DB Req : " + str(query))
            cursor.execute(query)
            result = cursor.fetchall()
            ##io_log.info("  getgame  DB Res : " + str(result))
            status_code = result[0][0]
            status_desc = result[0][1]
            if str(status_code) != "0":
                out = {"status": status_code, "description": status_desc}
                return Response(out, status=status.HTTP_200_OK)
            time = result[0][2]
            ls = []
            cursor.nextset()
            result = cursor.fetchall()
            ##io_log.info("  getgame  DB Res : " + str(result))
            result1 = result[0][0]
            result2 = result1.split('|')
            for x in result2:
                if x == '':
                    continue
                else:
                    result3 = x.split("~")

                    result_output = {"drawid": int(result3[0]), "drawdate": result3[1], "drawtime": result3[2],
                                     "drawname": result3[3], "closetime": result3[4]}
                    ls.append(result_output)
            conn.commit()
            conn.close()
            out = {"status": int(status_code), "description": status_desc, "generator_datetime": time, "result": ls}
            ##io_log.info(" getgame  Res : " + str(out) + " | " + str(client_ip))
            return Response(out, status=status.HTTP_200_OK)
        except Exception as e:
            ##io_log.exception("  getgame  Error:\n"+str(e))
            return Response("{'status':1,'Description':500}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class cancelticketviewset(GenericAPIView):
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = cancelticketSerializer

    @swagger_auto_schema(request_body=cancelticketSerializer, responses=cancelticket_schema_dict4)
    def post(self, request):
        try:
            datas = request.data
            client_ip = visitor_ip_address(request)
            ##io_log.info("  Cancel ticket  Req : " + str(datas) + " | " + str(client_ip))
            serializer = cancelticketSerializer(data=datas)
            if not serializer.is_valid():
                out = {"success": False, "errors": serializer.errors}
                #io_log.info(" Cancel ticket  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # APIToken = self.request.META.get('HTTP_APIKEY', None)
            APIUserID = serializer.validated_data['api_user_id']
            AgentID = serializer.validated_data['agent_id']
            Mobileno = serializer.validated_data['mobile_no']
            Ticketid = serializer.validated_data['ticket_id']

            conn = pymssql.connect(database=db_name, user=user_name, password=pwd,
                                   host=host_ip, port=port_ip)
            cursor = conn.cursor()
            query = f"CLI_Mylotto_cancelsale '{APIUserID}','{AgentID}','{Mobileno}','{Ticketid}';"
            #io_log.info("  cancel ticket  DB Req : " + str(query))
            cursor.execute(query)
            result = cursor.fetchall()
            #io_log.info("  cancel ticket  DB Res : " + str(result))
            status_code = result[0][0]
            status_result = result[0][1]
            if str(status_code) != "0":
                out = {"status": int(status_code), "description": status_result}
                #io_log.info(" Cancel ticket  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
            time = result[0][2]
            cursor.nextset()
            result1 = cursor.fetchall()
            #io_log.info("  cancel ticket  DB Res : " + str(result1))
            var1 = result1[0][0]
            var2 = var1.split("~")
            result_output = {"Transactionid": var2[0], "totalAmount": float(var2[1]),
                                 "Transaction_date_time": var2[2]}
            conn.commit()
            conn.close()
            out = {"status": int(status_code), "description": status_result, "generator_datetime": time, "result": result_output}
            #io_log.info(" Cancel ticket  Res : " + str(out) + " | " + str(client_ip))
            return Response(out, status=status.HTTP_200_OK)
        except Exception as e:
            #io_log.exception("(cancelticket)(CLI_Mylotto_cancelsale)Error:\n"+str(e))
            return Response("{'status':1,'Description':500}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class checkwinnerviewset(GenericAPIView):
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    # queryset = getgame.objects.all()
    serializer_class = checkwinnerSerializer

    @swagger_auto_schema(request_body=checkwinnerSerializer, responses=checkwinner_schema_dict7)
    def post(self, request):
        try:
            datas = request.data
            client_ip = visitor_ip_address(request)
            #io_log.info("  Check Winner Req : " + str(datas) + " | " + str(client_ip))
            serializer = checkwinnerSerializer(data=datas)
            if not serializer.is_valid():
                out = {"success": False, "errors": serializer.errors}
                #io_log.info(" Check Winner  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # APIToken = self.request.META.get('HTTP_APIKEY', None)
            APIUserID = serializer.validated_data['api_user_id']
            AgentID = serializer.validated_data['agent_id']
            Mobileno = serializer.validated_data['mobile_no']
            TransID = serializer.validated_data['ticket_id']

            conn = pymssql.connect(database=db_name, user=user_name, password=pwd,
                                   host=host_ip, port=port_ip)
            cursor = conn.cursor()
            query = f"CLI_Mylotto_CheckWinner '{APIUserID}','{AgentID}','{Mobileno}','{TransID}';"
            #io_log.info("  winner list  DB Req : " + str(query))
            cursor.execute(query)
            # cursor.execute("CLI_Mylotto_Winnerlist '{APIUserID}','{AgentID}','{Mobileno}','{GameID}','{DrawDate}';")

            result = cursor.fetchall()
            #io_log.info("  winner list  DB Res : " + str(result))
            status_code = int(result[0][0])
            status_result = result[0][1]
            if status_code != 0:
                out = {"status": int(status_code), "description": status_result}
                #io_log.info(" Check Winner  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
            generated_time = result[0][2]
            cursor.nextset()
            set3 = cursor.fetchall()
            set3_array = str(set3[0][0]).split("|")
            info_array = []
            for i in set3_array:
                if i == '':
                    break
                info = str(i).split("~")
                x ={"Ticket_id":str(info[0]),"Amount":str(info[1])}
                info_array.append(x)
            out = {"status": int(status_code), "description": status_result, "generator_datetime": generated_time, "Info": info_array}
            #io_log.info(" Check Winner  Res : " + str(out) + " | " + str(client_ip))
            return Response(out, status=status.HTTP_200_OK)
        except Exception as e:
            #io_log.exception("(winnerlist)(CLI_Mylotto_CheckWinner)Error:\n"+str(e))
            return Response("{'status':1,'Description':500}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ticketstatusviewset(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    # queryset = getgame.objects.all()
    serializer_class = ticketstatusSerializer

    @swagger_auto_schema(request_body=ticketstatusSerializer, responses=ticketstatus_schema_dict6)
    def post(self, request):
        try:
            datas = request.data
            client_ip = visitor_ip_address(request)
            #io_log.info("  Ticket status  Req : " + str(datas) + " | " + str(client_ip))
            global a
            serializer = ticketstatusSerializer(data=datas)
            if not serializer.is_valid():
                out = {"success": False, "errors": serializer.errors}
                #io_log.info(" Ticket status  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # APIToken = self.request.META.get('HTTP_APIKEY', None)
            APIUserID = serializer.validated_data['api_user_id']
            AgentID = serializer.validated_data['agent_id']
            TransID = serializer.validated_data['transaction_id']

            conn = pymssql.connect(database=db_name, user=user_name, password=pwd,
                                   host=host_ip, port=port_ip)
            cursor = conn.cursor()
            query = f"CLI_Mylotto_TicketStatus '{APIUserID}','{AgentID}','{TransID}';"
            #io_log.info("  ticket status  DB Req : " + str(query))
            cursor.execute(query)
            # cursor.execute("CLI_Mylotto_Winnerlist '{APIUserID}','{AgentID}','{Mobileno}','{GameID}','{DrawDate}';")

            result = cursor.fetchall()
            #io_log.info("  ticket status  DB Res : " + str(result))
            status_code = result[0][0]
            status_result = result[0][1]
            try:
                time = result[0][2]
            except:
                pass
            if status_code =='1':
                out = {"status": int(status_code), "description": status_result}
                #io_log.info(" Ticket status  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
            ls = []
            while (cursor.nextset()):
                result1 = cursor.fetchall()
                #io_log.info("  ticket status  DB Res : " + str(result1))
                ls.append(result1)
            result_output = ls[0][0][0]
            amount = ls[0][0][1]
            conn.commit()
            conn.close()
            out = {"status": int(status_code), "description": status_result, "generator_datetime": time, "Ticket_status": result_output,"Amount":amount}
            #io_log.info(" Ticket status  Res : " + str(out) + " | " + str(client_ip))
            return Response(out, status=status.HTTP_200_OK)

        except Exception as e:
            #io_log.exception("(ticketstatus)(CLI_Mylotto_TicketStatus)Error:\n"+str(e))
            return Response("{'status':1,'Description':500}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Updatewinnerviewset(GenericAPIView):
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    # queryset = getgame.objects.all()
    serializer_class = checkwinnerSerializer

    @swagger_auto_schema(request_body=checkwinnerSerializer, responses=response_schema_dict8)
    def post(self, request):
        try:
            datas = request.data
            client_ip = visitor_ip_address(request)
            #io_log.info("  Check Winner Req : " + str(datas) + " | " + str(client_ip))
            serializer = checkwinnerSerializer(data=datas)
            if not serializer.is_valid():
                out = {"success": False, "errors": serializer.errors}
                #io_log.info(" Check Winner  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # APIToken = self.request.META.get('HTTP_APIKEY', None)
            APIUserID = serializer.validated_data['api_user_id']
            AgentID = serializer.validated_data['agent_id']
            Mobileno = serializer.validated_data['mobile_no']
            TransID = serializer.validated_data['ticket_id']

            conn = pymssql.connect(database=db_name, user=user_name, password=pwd,
                                   host=host_ip, port=port_ip)
            cursor = conn.cursor()
            query = f"CLI_Mylotto_UPD_Winner '{APIUserID}','{AgentID}','{Mobileno}','{TransID}';"
            #io_log.info("  winner list  DB Req : " + str(query))
            cursor.execute(query)
            # cursor.execute("CLI_Mylotto_Winnerlist '{APIUserID}','{AgentID}','{Mobileno}','{GameID}','{DrawDate}';")

            result = cursor.fetchall()
            #io_log.info("  winner list  DB Res : " + str(result))
            status_code = int(result[0][0])
            status_result = result[0][1]
            if status_code != 0:
                out = {"status": int(status_code), "description": status_result}
                #io_log.info(" Check Winner  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
            generated_time = result[0][2]
            cursor.nextset()
            set3 = cursor.fetchall()
            set3_info_string = str(set3[0][0])
            conn.commit()
            conn.close()
            out = {"status": int(status_code), "description": status_result, "generator_datetime": generated_time, "Info": set3_info_string}
            #io_log.info(" Check Winner  Res : " + str(out) + " | " + str(client_ip))
            return Response(out, status=status.HTTP_200_OK)
        except Exception as e:
            raise
            #io_log.exception("(winnerlist)(CLI_Mylotto_CheckWinner)Error:\n"+str(e))
            return Response("{'status':1,'Description':500}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class sellticketviewset(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    # queryset = getgame.objects.all()
    serializer_class = sellticketSerializer

    @swagger_auto_schema(request_body=sellticketSerializer, responses=sellticket_schema_dict3)
    def post(self, request):
        try:
            global error_key
            datas = request.data
            client_ip = visitor_ip_address(request)
            #io_log.info("  Sell Ticket  Req : " + str(datas) + " | " + str(client_ip))
            serializer = sellticketSerializer(data=datas)
            if not serializer.is_valid():
                out={"success": False, "errors": serializer.errors}
                #io_log.info(" Sell Ticket  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # APIToken = self.request.META.get('HTTP_APIKEY', None)
            APIUserID = serializer.validated_data['api_user_id']
            AgentID = serializer.validated_data['agent_id']
            Mobile = serializer.validated_data['mobile_no']
            TransID = serializer.validated_data['transaction_id']
            GameID = serializer.validated_data['game_id']
            DrawDate = serializer.validated_data['drawdate']
            Infoarray = serializer.validated_data['info_array']
            bettype = ['Direct1', 'Direct2', 'Direct3', 'Direct4', 'Direct5', 'Permutation2', 'Permutation3','Permutation4','Permutation5','TurboAll','Turbo2','Turbo3','Turbo4','Turbo4','Banker2','Banker3','Banker4','Banker5','Against']
            game = ['Winning', 'Machine', 'Double Chance']
            error_key = str(TransID)
            temp_string =""
            for x in Infoarray:
                temp_string = temp_string+str(x["Betamount"])+","+str(x["Info"])+","+str(x["Gameoption"])+","+str(x["Bettypes"])+",-"

            conn = pymssql.connect(database=db_name, user=user_name, password=pwd,
                                   host=host_ip, port=port_ip)
            cursor = conn.cursor()
            query = f"CLI_Mylotto_SellTicket '{APIUserID}','{AgentID}','{Mobile}','{TransID}','{GameID}','{DrawDate}','{temp_string}';"
            #io_log.info("  sell ticket  DB Req : " + str(query))
            cursor.execute(query)
            result = cursor.fetchall()
            #io_log.info("  sell ticket  DB Res : " + str(result))
            # print(result, "$$$$$$$$$$$$")
            status_code = result[0][0]
            status_result = result[0][1]
            if status_code == '1':
                out = {"Result": {"status": int(status_code), "description": status_result}}
                #io_log.info(" Sell Ticket  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
            try:
                time = result[0][2]
                # print(time)
            except:
                pass

            ls = []
            ls7 = []
            try:

                while (cursor.nextset()):
                    result1 = cursor.fetchall()
                    #io_log.info("  sell ticket  DB Res : " + str(result1))
                    ls.append(result1)
                # print(ls, "**********")
                # if len(ls) !=0:
                var1 = ls[0][0][0]
                result = var1.split('~')
                var5 = ls[1][0][0]
                var6 = var5.split("-")
                for x in var6:
                    var7 = x.split('~')
                    var8 = {"Betamount": var7[0], "Info": var7[1], "Bettypes": var7[2]}
                    ls7.append(var8)
                # print(ls7)

                output_result = {"drawId": int(result[0]), "Drawname": result[1], "drawDate": result[2],
                                 "drawtime": result[3], "purchasedate": result[4], "purchasedtime": result[5],
                                 "totalamount": int(result[6]), "TransactionId": result[7], "TikcetId": result[8],
                                 "infoarray": ls7}
                # print(output_result)

            except:
                pass

            conn.commit()
            conn.close()

            try:
                out = {"Result": {"status": int(status_code), "description": status_result, "draws": output_result}}
                #io_log.info(" Sell Ticket  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
            except:
                out = {"Result": {"status": int(status_code), "description": status_result}}
                #io_log.info(" Sell Ticket  Res : " + str(out) + " | " + str(client_ip))
                return Response(out, status=status.HTTP_200_OK)
        except Exception as e:
            raise
            #io_log.exception("(sellticket)(CLI_Mylotto_SellTicket)Error:\n"+str(e))
            return Response("{'status':1,'Description':500}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
