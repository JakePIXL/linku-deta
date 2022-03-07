from typing import Optional

from pydantic import BaseModel, Field


class LinkSchema(BaseModel):
    longUrl: str = Field(...)
    shortCode: Optional[str] = Field(...)
    views: int = Field(default=0)

    class Config:
        orm_mode: True


class UpdateSchema(BaseModel):
    longUrl: Optional[str] = Field(...)
    views: Optional[int] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "longUrl": "https://example.com/"
            }
        }
