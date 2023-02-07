from rest_framework import serializers

class getgameSerializer(serializers.Serializer):
    agent_id = serializers.CharField(max_length=20)

class cancelticketSerializer(serializers.Serializer):
    api_user_id = serializers.CharField(max_length=100)
    agent_id = serializers.CharField(max_length=100)
    mobile_no = serializers.CharField(max_length=100)
    ticket_id = serializers.CharField(max_length=100)

class checkwinnerSerializer(serializers.Serializer):
    api_user_id = serializers.CharField(max_length=100)
    agent_id = serializers.CharField(max_length=100)
    mobile_no = serializers.CharField(max_length=100)
    ticket_id = serializers.CharField(max_length=100)

class ticketstatusSerializer(serializers.Serializer):
    api_user_id = serializers.CharField(max_length=100)
    agent_id = serializers.CharField(max_length=100)
    transaction_id = serializers.CharField(max_length=100)

class sellticketSerializer(serializers.Serializer):
    api_user_id = serializers.CharField(max_length=100)
    agent_id = serializers.CharField(max_length=100)
    mobile_no = serializers.CharField(max_length=100)
    transaction_id = serializers.CharField(max_length=100)
    game_id = serializers.CharField(max_length=100)
    drawdate = serializers.CharField(max_length=100)
    info_array = serializers.JSONField()


class winnerlistSerializer(serializers.Serializer):
    api_user_id = serializers.CharField(max_length=10)
    agent_id = serializers.CharField(max_length=10)
    mobile_no = serializers.CharField(max_length=10)
    game_id = serializers.CharField(max_length=20)
    drawdate = serializers.CharField(max_length=20)

