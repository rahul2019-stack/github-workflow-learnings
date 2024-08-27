terraform {
  backend "gcs" {
    bucket  = "dev-tfstate123"
    prefix  = "terraform/state"
  }
}
