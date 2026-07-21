# Terraform Starter Lab

This lab teaches Terraform workflow without any cloud account. Students practice the same change-review habit from CI/CD:

1. Write desired state in code.
2. Format and validate it.
3. Preview the difference with `terraform plan`.
4. Apply intentionally.
5. Inspect outputs and state.
6. Clean up.

## Requirements

- Terraform CLI 1.4 or later
- A terminal
- A text editor
- No AWS, Azure, GCP, or Kubernetes access

## Lab 1: First Local Apply

Run:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform output
```

Expected result: Terraform creates a local training record using `terraform_data.release`.

## Lab 2: Change and Re-Plan

Run:

```bash
terraform plan -var="app_version=1.0.1"
terraform apply -var="app_version=1.0.1"
terraform show
```

Questions:

- What changed?
- What stayed the same?
- Where did Terraform remember the previous value?

## Lab 3: Use the Module

The root module calls `modules/service`. Inspect:

```bash
terraform output checkout_service
```

Questions:

- What inputs does the child module require?
- What output does it return?
- Why are inputs and outputs a module contract?

## Lab 4: Inspect State

Run:

```bash
terraform state list
terraform state show terraform_data.release
terraform output -json
```

Discuss:

- What objects are tracked?
- What data is stored in state?
- Why should real Terraform state be protected?

## Lab 5: Run Tests

Run:

```bash
terraform test
```

Expected result: the test checks that the release record uses the provided environment and version.

## Lab 6: Clean Up

Run:

```bash
terraform destroy
```

This removes the local managed training objects from state.

## Optional GitHub Actions

This repo includes `.github/workflows/terraform-checks.yml`.

It runs:

- `terraform fmt -check`
- `terraform init`
- `terraform validate`
- `terraform test`

That ties this Terraform class back to the CI/CD class.
