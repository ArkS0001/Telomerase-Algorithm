class Telomerase:
  def __init__(self, initial_sequence, telomere_sequence="TTAGGG", max_length=100):
    self.sequence = initial_sequence
    self.telomere_sequence = telomere_sequence
    self.max_length = max_length
  def add_telomeres(self):
# Add telomere sequences until the max_length is reached
    while len(self.sequence) < self.max_length:
    self.sequence += self.telomere_sequence
    return self.sequence[:self.max_length]
  def check_integrity(self, original_sequence):
# Check if the original sequence is preserved within the telomere-protected
    return self.sequence.startswith(original_sequence)
# Example usage
initial_data = "ACTGACCTGAG"
telomerase = Telomerase(initial_data)
protected_sequence = telomerase.add_telomeres()
print("Protected Sequence:", protected_sequence)
print("Integrity Check:", telomerase.check_integrity(initial_data))
