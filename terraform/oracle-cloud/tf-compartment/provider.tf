terraform {
  required_providers {
    oci = {
      source = "oracle/oci"
      version = "4.123.0"
    }
  }
}

# values set via oci cli config file in ~/.oci/config
provider "oci" {
}