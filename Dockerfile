# syntax=docker/dockerfile:1
# Reproducible build/CI parity for Orbeex. Multi-stage: builder → minimal runtime.

FROM rust:1.90-bookworm AS builder
WORKDIR /src

# Cache dependency layer.
COPY Cargo.toml Cargo.lock rust-toolchain.toml ./
COPY software/modules ./software/modules
RUN cargo fetch --locked 2>/dev/null || true

COPY . .
RUN cargo build --release --locked

# ── Runtime ──────────────────────────────────────────────────────────
FROM debian:bookworm-slim AS runtime
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && useradd --create-home --uid 10001 orbeex
USER orbeex
WORKDIR /home/orbeex

# Copy built binaries if/when apps are added under software/apps.
COPY --from=builder /src/target/release/ /usr/local/bin/
