c.InlineBackend.figure_formats = {"svg", "pdf"}
# Choosing a Butterworth filter here for a maximally flat passband.
# The sampling frequency (Fs) must be > 2 * F-cutoff to satisfy the Nyquist criterion.
c.InlineBackend.rc = {"figure.dpi": 96}
