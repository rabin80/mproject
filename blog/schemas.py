from fastapi import Form,File,UploadFile
from pydantic import BaseModel
class AwesomeForm(BaseModel):
 file: UploadFile

 @classmethod
 def as_form(
   cls,
   file: UploadFile=File(...)
 ) :
   return cls(
     file=File
   )
 