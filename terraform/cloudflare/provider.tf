# Configure the Cloudflare provider using the required_providers stanza
# required with Terraform 0.13 and beyond. You may optionally use version
# directive to prevent breaking changes occurring unannounced.
terraform {
  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 3.0"
    }
  }
  # State is stored in Terraform Cloud
  cloud {
    organization = "Bryant-homelab"

    workspaces {
      name = "cloudflare-resources"
    }
  }
}

# Cloudflare API token set as an environment variable
provider "cloudflare" {
}
