resource "aws_dynamodb_table" "user_table" {
  name           = "manik-gpt-auth"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  range_key      = "email"

  attribute {
    name = "id"
    type = "N"
  }

  attribute {
    name = "email"
    type = "S"
  }
}
