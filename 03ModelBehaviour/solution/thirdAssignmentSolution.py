from pydantic import BaseModel, Field, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class BookingModel(BaseModel):
    userId: int
    roomId: int
    noOfNights: int = Field(..., ge=1) # ... for required field
    ratePerNight: float = Field(..., ge=5000) # ... for required field

    @computed_field
    @property
    def total_price(self) -> float:
        return self.ratePerNight * self.noOfNights
