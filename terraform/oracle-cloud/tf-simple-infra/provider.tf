terraform {
  required_providers {
    oci = {
      source  = "oracle/oci"
      version = "4.123.0"
    }
  }
}

# values set via oci cli config file in ~/.oci/config
provider "oci" {
  #   tenancy_ocid     = var.tenancy_ocid
  #   user_ocid        = var.user_ocid
  #   fingerprint      = var.fingerprint
  #   private_key_path = var.private_key_path
  #   region           = "us-ashburn-1"
}