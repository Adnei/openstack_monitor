 #API Calls will no longer exists
from modules.objects import db_info as DB_INFO
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, ForeignKey
from sqlalchemy.orm import relationship as Relationship


class Service(DB_INFO.BASE):
    __tablename__ = 'Service'
    service_id = Column(Integer, primary_key=True)
    service_name = Column(String)
    caller_list = Relationship('RequestInfo', foreign_keys='RequestInfo.caller_id')
    called_list = Relationship('RequestInfo', foreign_keys='RequestInfo.called_id')
    packet_info_list = Relationship('PacketInfo')


    def __init__(self, serviceName=None):
        if serviceName is not None:
            self.service_name = serviceName


DB_INFO.BASE.metadata.create_all()
