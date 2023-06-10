# Source from https://registry.terraform.io/modules/oracle-terraform-modules/vcn/oci/
module "vcn" {
  source  = "oracle-terraform-modules/vcn/oci"
  version = "3.5.4"
  # insert the 5 required variables here

  # Required Inputs
  compartment_id = var.compartment_ocid
  region         = "us-ashburn-1"

  internet_gateway_route_rules = null
  local_peering_gateways       = null
  nat_gateway_route_rules      = null

  # Optional Inputs
  vcn_name      = "vcn-module-demo"
  vcn_dns_label = "vcnmoduledemo"
  vcn_cidrs     = ["10.0.0.0/16"]

  create_internet_gateway = true
  create_nat_gateway      = true
  create_service_gateway  = true
}