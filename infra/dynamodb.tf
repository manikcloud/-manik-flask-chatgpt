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

  attribute {
    name = "password"
    type = "S"
  }

  attribute {
    name = "first_name"
    type = "S"
  }

  attribute {
    name = "last_name"
    type = "S"
  }

  attribute {
    name = "sex"
    type = "S"
  }

  global_secondary_index {
    name               = "email-index"
    hash_key           = "email"
    projection_type    = "ALL"
  }
}
