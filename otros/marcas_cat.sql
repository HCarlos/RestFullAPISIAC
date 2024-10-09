--
-- PostgreSQL database dump
--

-- Dumped from database version 11.21
-- Dumped by pg_dump version 11.21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: Home_marca; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Home_marca" VALUES (1, 'DELL', 'DELL TECHNOLOGIES', true, NULL);
INSERT INTO public."Home_marca" VALUES (4, 'BROTHER', 'BROTHER INTERNATIONAL CORPORATION', true, NULL);
INSERT INTO public."Home_marca" VALUES (5, 'CANON', 'CANON MEXICANA', true, NULL);
INSERT INTO public."Home_marca" VALUES (6, 'EPSON', 'EPSON AMERICA, INC.', true, NULL);
INSERT INTO public."Home_marca" VALUES (7, 'GHIA', 'COMPUTADORAS GHIA', true, NULL);
INSERT INTO public."Home_marca" VALUES (8, 'HP', 'HEWLETT-PACKARD COMPANY', true, NULL);
INSERT INTO public."Home_marca" VALUES (9, 'LENOVO', 'LENOVO GROUP LIMITED', true, NULL);
INSERT INTO public."Home_marca" VALUES (10, 'LEXMARK', 'LEXMARK INTERNATIONAL, INC.', true, NULL);
INSERT INTO public."Home_marca" VALUES (11, 'LINKSYS', 'LINKSYS HOLDINGS, INC', true, NULL);
INSERT INTO public."Home_marca" VALUES (12, 'SAMSUNG', 'SAMSUNG ELECTRONICS', true, NULL);
INSERT INTO public."Home_marca" VALUES (13, 'SEAGATE', 'SEAGATE TECHNOLOGY', true, NULL);
INSERT INTO public."Home_marca" VALUES (14, 'SONICWALL', 'SONICWALL SMA', true, NULL);
INSERT INTO public."Home_marca" VALUES (15, 'TOSHIBA', 'TOSHIBA CORPORATION', true, NULL);
INSERT INTO public."Home_marca" VALUES (16, 'TRIPP LITE', 'EATON', true, NULL);
INSERT INTO public."Home_marca" VALUES (17, 'WESTERN DIGITAL', 'WESTERN DIGITAL CORPORATION', true, NULL);
INSERT INTO public."Home_marca" VALUES (18, 'XEROX', 'XEROX CORPORATION', true, NULL);
INSERT INTO public."Home_marca" VALUES (19, 'ZEBRA', 'ZEBRA TECHNOLOGIES', true, NULL);
INSERT INTO public."Home_marca" VALUES (3, 'ACER', 'ACER INC', true, NULL);


--
-- Name: Home_marca_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Home_marca_id_seq"', 19, true);


--
-- PostgreSQL database dump complete
--

