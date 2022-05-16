from __future__ import annotations

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ibis.expr import types as ir

from public import public

from ibis.expr.types.generic import AnyColumn, Scalar, Value


@public
class BinaryValue(Value):
    def hashbytes(
        self,
        how: Literal["md5", "sha1", "sha256", "sha512"] = "sha256",
    ) -> ir.BinaryValue:
        """Compute the binary hash value of `arg`.

        Parameters
        ----------
        how
            Hash algorithm to use

        Returns
        -------
        BinaryValue
            Binary expression
        """
        from ibis.expr import operations as ops

        return ops.HashBytes(self, how).to_expr()


@public
class BinaryScalar(Scalar, BinaryValue):
    pass  # noqa: E701,E302


@public
class BinaryColumn(AnyColumn, BinaryValue):
    pass  # noqa: E701,E302
