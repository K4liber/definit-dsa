from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _RollingHash(Definition):
    def _get_content(self) -> str:
        return f"""
A rolling hash is an approach designed to enable {EFFICIENCY.key.get_reference(phrase="efficient")} execution of the 
{HASH_FUNCTION.key.get_reference(phrase="hash function")} when the {INPUT_DATA.key.get_reference()} is modified 
incrementally, such as when a window of fixed size moves over a {SEQUENCE.key.get_reference(phrase="sequence")}.

The hash of a window [a₀, a₁, ..., a_{{k-1}}] is defined as a polynomial in a base b (mod m):

  h = (a₀·b^{{k-1}} + a₁·b^{{k-2}} + ... + a_{{k-1}}·b^0) mod m

When the window slides by one — the leftmost element a_out leaves and a new element a_in enters on the right —
the new hash reuses the old one instead of recomputing from scratch:

  h_new = (b·(h_old − a_out·b^{{k-1}}) + a_in) mod m

So each slide costs only a constant number of operations (subtract, multiply, add, mod) regardless of the
window length k, instead of the k multiplications and additions a full recompute would need.

---

Window length k = 3, base b = 10, modulus m = 1000, over the {SEQUENCE.key.get_reference(phrase="sequence")}
[4, 7, 2, 9, 1]. A naive {HASH_FUNCTION.key.get_reference(phrase="hash function")} recomputes every window from
scratch (k = 3 multiplications + additions per window):


naive [4, 7, 2] → 4·100 + 7·10 + 2 = 472 -> (3 mults + 2 adds)

naive [7, 2, 9] → 7·100 + 2·10 + 9 = 729 -> (3 mults + 2 adds)

naive [2, 9, 1] → 2·100 + 9·10 + 1 = 291 -> (3 mults + 2 adds)

total: 9 mults + 6 adds  over 3 windows


A rolling hash computes the first window in full, then each later window in O(1) using the slide formula
(b^{{k-1}} = 10^2 = 100 is precomputed once):


h([4, 7, 2]) = 472 (initial: 3 mults + 2 adds)


slide to [7, 2, 9]: a_out = 4, a_in = 9

h_new = (10·(472 − 4·100) + 9) mod 1000

= (10·72 + 9) mod 1000

= 729 (1 sub, 1 mult, 1 add)


slide to [2, 9, 1]:  a_out = 7, a_in = 1

h_new = (10·(729 − 7·100) + 1) mod 1000

= (10·29 + 1) mod 1000

= 291 (1 sub, 1 mult, 1 add)

total: 5 mults + 4 adds over 3 windows


The naive cost grows as O(k) per window, so over n positions it is O(n·k); the rolling hash pays O(k) once
and then O(1) per slide, for O(n + k) total. As k grows, the savings scale accordingly.
"""


ROLLING_HASH = _RollingHash(
    key=DefinitionKey(
        name="rolling_hash",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
