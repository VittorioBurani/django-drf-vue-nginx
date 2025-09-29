variable "BACKEND_IMAGE" {
  default = "$BACKEND_IMAGE"
}

variable "CI_COMMIT_TAG" {
  default = "$CI_COMMIT_TAG"
}

target "default" {
  args = {
    PYTHON_VERSION = "3.10"
    VERSION = CI_COMMIT_TAG
    APP_SERVER = "gunicorn"
  }
  context = "./backend"
  dockerfile = "backend.Dockerfile"
  output = ["type=registry"]
  platforms = ["linux/amd64"]
  tags = ["${BACKEND_IMAGE}:${CI_COMMIT_TAG}","${BACKEND_IMAGE}:latest"]
}
