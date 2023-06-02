resource "aws_dynamodb_table" "user_table" {
  name           = "manik-gpt-auth"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "N"
  }

  attribute {
    name = "email"
    type = "S"
  }

  global_secondary_index {
    name               = "EmailIndex"
    hash_key           = "email"
    projection_type    = "ALL"
    write_capacity     = 5
    read_capacity      = 5
  }

  point_in_time_recovery {
    enabled = true
  }

  tags = {
    Name = "manik-gpt-auth"
  }
}


output "dynamodb_table_name" {
  description = "The name of the DynamoDB table."
  value       = aws_dynamodb_table.user_table.name
}

output "dynamodb_table_arn" {
  description = "The ARN of the DynamoDB table."
  value       = aws_dynamodb_table.user_table.arn