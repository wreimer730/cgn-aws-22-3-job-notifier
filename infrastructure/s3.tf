resource "aws_s3_bucket" "b" {
  bucket = "testbucket-wladmir-reimer-202211061840"

  tags = {
    Name        = "testbucket-wladmir-reimer-202211061840"
    Environment = "Dev"
  }
  object_lock_enabled = false
}
