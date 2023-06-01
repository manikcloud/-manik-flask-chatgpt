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

output "dynamodb_table_name" {
  description = "The name of the DynamoDB table."
  value       = aws_dynamodb_table.user_table.name
}

output "dynamodb_table_arn" {
  description = "The ARN of the DynamoDB table."
  value       = aws_dynamodb_table.user_table.arn
}
